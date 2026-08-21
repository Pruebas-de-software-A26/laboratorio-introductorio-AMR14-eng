import logging
import operations  

logging.basicConfig(
  level=logging.INFO,
  filemode= "w",
  filename="test.log"
  )

if __name__ == "__main__":

    logging.info("TEST CASE 1")
    result = operations.add(1, 2)

    if result == 3:
        logging.info("PASS")
    else:
        logging.error("FAIL")

    logging.info("TEST CASE 2")
    result2 = operations.power(2, 2)

    if result2 == 4:
        logging.info("PASS")
    else:
        logging.error("FAIL")



  # logging.info(f"Result: {result}")
  # logging.warning("Division Imposible")
  # logging.error("Error")
  # logging.debug("The value i a and b is...")
  # logging.critical("Critical in time")
