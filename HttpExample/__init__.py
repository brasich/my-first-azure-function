import logging
import numpy as np

import azure.functions as func


def main(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    input_num = req.params.get('input_num')
    if not input_num:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            input_num = req_body.get('input_num')
        

    if input_num:
        msg.set(input_num)
        resp_string = f"""
            Input Number: {input_num}
            Input Num * 2: {int(input_num) * 2}
            This could easily be a model not just simple multiplication
            Random number from numpy just to show package installations working: {np.random.random()}
        """
        return func.HttpResponse(resp_string)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a number in the query string as 'input_num' for a demo.",
             status_code=200
        )
