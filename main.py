import logging
import operations  

logging.basicConfig(
  level=logging.INFO,
  filemode= "w",
  filename="test.log"
  )

if __name__ == "__main__":

    logging.info("TEST CASE 1 - ADD")
    result = operations.add(1, 2)

    if result == 3:
        logging.info("PASS")
    else:
        logging.error("FAIL")


    logging.info("TEST CASE 2 - SUBTRACT")
    result = operations.subtract(5, 2)

    if result == 3:
        logging.info("PASS")
    else:
        logging.error("FAIL")


    logging.info("TEST CASE 3 - MULTIPLY")
    result = operations.multiply(3, 4)

    if result == 12:
        logging.info("PASS")
    else:
        logging.error("FAIL")


    logging.info("TEST CASE 4 - DIVIDE")
    result = operations.divide(10, 2)

    if result == 5:
        logging.info("PASS")
    else:
        logging.error("FAIL")


    logging.info("TEST CASE 5 - POWER")
    result = operations.power(2, 3)

    if result == 8:
        logging.info("PASS")
    else:
        logging.error("FAIL")


    logging.info("TEST CASE 6 - SQUARE ROOT")
    result = operations.square_root(16)

    if result == 4:
        logging.info("PASS")
    else:
        logging.error("FAIL")


    logging.info("TEST CASE 7 - AVERAGE")
    result = operations.average([2, 4, 6, 8])

    if result == 5:
        logging.info("PASS")
    else:
        logging.error("FAIL")


    logging.info("TEST CASE 8 - MAXIMUM")
    result = operations.maximum([2, 8, 4, 6])

    if result == 8:
        logging.info("PASS")
    else:
        logging.error("FAIL")



  # logging.info(f"Result: {result}")
  # logging.warning("Division Imposible")
  # logging.error("Error")
  # logging.debug("The value i a and b is...")
  # logging.critical("Critical in time")
