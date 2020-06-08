class DatabaseConnectionError(Exception):
    msg = "Unable to Establish Connection with Database"

    def __init__(self):
        super().__init__(self.msg)

class TableNotFoundError(Exception):
    msg = "Table Not Found"

    def __init__(self):
        super().__init__(self.msg)

class FilenameError(Exception):
    msg = "Please select a File to Save the TempSweep Data to"

    def __init__(self):
        super().__init__(self.msg)

class NoConnectionError(Exception):
    msg = "There is no connection with the sensor"

    def __init__(self):
        super().__init__(self.msg)

class NoSensorSNError(Exception):
    msg = "Please Enter a Sensor SN"

    def __init__(self):
        super().__init__(self.msg)

class NoModuleSNError(Exception):
    msg = "Please Enter a Module SN"

    def __init__(self):
        super().__init__(self.msg)

class NoTechInitialsError(Exception):
    msg = "Please Select Technician Initials"

    def __init__(self):
        super().__init__(self.msg)

class NoPPMError(Exception):
    msg = "Please Enter A PPM Reading"

    def __init__(self):
        super().__init__(self.msg)


class BaselineAlreadyUpdated(Exception):
    msg = "The Baseline Table has already had elements removed"

    def __init__(self):
        super().__init__(self.msg)

class BaselineAlreadyRestored(Exception):
    msg = "The Baseline Table has already been restored"

    def __init__(self):
        super().__init__(self.msg)

class BaselineNotPreviouslyAltered(Exception):
    msg = "The Baseline Table was not previously altered"

    def __init__(self):
        super().__init__(self.msg)

class DatabaseNotConnected(Exception):
    msg = "Not Connected to the Production Database"

    def __init__(self):
        super().__init__(self.msg)

class BaselineTableNotPresent(Exception):
    msg = "The Custom Baseline Table is not present in the Database"

    def __init__(self):
        super().__init__(self.msg)