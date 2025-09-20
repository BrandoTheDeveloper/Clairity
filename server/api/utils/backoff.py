from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
import httpx

def backoffable():
    return retry(
        reraise=True,
        retry=retry_if_exception_type((httpx.HTTPError, TimeoutError)),
        wait=wait_exponential(multiplier=0.5, min=0.5, max=8),
        stop=stop_after_attempt(4),
    )
