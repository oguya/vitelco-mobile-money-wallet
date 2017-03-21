import uuid
from datetime import datetime
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from structlog import get_logger
from app_dir.bill_management.models import Bill

logger = get_logger("bills")


def send_error_response(message="404",
                        key="msisdn",
                        value=None,
                        status=None,
                        ):
    """
    Creates and outputs given error message
    Parameters
    ----------
    message : error message
    key : key errorParameter
    value: value errorParameter
    status: status code
    Returns
    -------
    a application/json rest_framework.response
    """
    date_time = datetime.now().isoformat()
    error_payload = {
        "errorCategory": "businessRule",
        "errorCode": "genericError",
        "errorDescription": message,
        "errorDateTime": date_time,
        "errorParameters": [
            {
                "key": key,
                "value": value
            }
        ]
    }

    response = Response(data=error_payload,
                        status=status
                        )
    return response


class CreateBillPayment(APIView):
    """
    This API posts a bill payment given a billReference

    Headers:
    `Content-Type: application/json,
     Accept: application/json,
     Date: 21-03-2017,
     X-CorrelationID: afc71b32-9a8d-4260-8cdc-c6f452b9b09f`

    Example payload:
    {
        "currency": "KES",
        "amount": "10000",
        "minAmountDue": "1",
        "dueDate": "2017-02-28 16:00:00",
        "billReference": "afc71b32-9a8d-4260-8cdc-c6f452b9b09f",
        "debitParty": [
        {
        "key": "msisdn",
        "value": "+4491509874561"
        }],
        "creditParty": [
        {
        "key": "msisdn",
        "value": "+25691508523697"
        }]
        }
    """

    def post(self, request, bill_reference):
        error_message = None
        error_key = None
        try:
            server_correlation_id = request.META['HTTP_X_CORRELATIONID']
            date = request.META["HTTP_DATE"]
        except KeyError as e:
            logger.info("create_transaction_400",
                        message="Required Headers not supplied",
                        status=status.HTTP_400_BAD_REQUEST,
                        key=e.message
                        )
            return send_error_response(
                message="Required Headers not supplied",
                key=e.message,
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            data = request.data
            biller = data["creditParty"][0]["value"]
            billee = data["debitParty"][0]["value"]
            amount_due = data["amount"]
            currency = data["currency"]
            bill_reference = bill_reference
            due_date = data["dueDate"]

            create_bill_data = dict(
                biller=biller,
                billee=billee,
                bill_reference=bill_reference,
                amount_due=amount_due,
                currency=currency,
                due_date=due_date
            )


        except KeyError as e:
            error_message = "Missing required field"
            key = e.message
            value = None
            status_code = status.HTTP_400_BAD_REQUEST
            error_response = send_error_response(
                message=error_message,
                key=key,
                value=value,
                status=status_code
            )

            logger.info("create_bill_400",
                        status=status.HTTP_400_BAD_REQUEST,
                        key=key
                        )

            return error_response
        else:
            bill = self.create_bill(create_bill_data)
            if bill:
                response_payload = {
                    "objectReference": bill_reference,
                    "serverCorrelationId": server_correlation_id,
                    "status": "pending",
                    "notificationMethod": "callback",
                    "expiryTime": "",
                    "pollLimit": 0,
                    "error": None

                }
            logger.info("create_transaction_202",
                        status=status.HTTP_202_ACCEPTED,
                        bill_reference=bill_reference,
                        response_payload=response_payload
                        )
            return Response(response_payload,
                            status=status.HTTP_202_ACCEPTED
                            )

    @staticmethod
    def create_bill(create_bill_data):
        try:
            transaction = Bill.objects.create(**create_bill_data)
            logger.info("create_transaction_success",
                        bill_reference=create_bill_data.get('bill_reference')
                        )
            return True, transaction
        except IntegrityError as e:
            exception = str(e).split("DETAIL:")[1]
            logger.info("create_transaction_duplicate_uuid",
                        exception=exception,
                        )
            return False, exception
