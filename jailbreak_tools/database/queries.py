GET_TECHNICIANS = """SELECT Fullname from TechNames"""
GET_TECH_INITIALS = """SELECT Initials from TechNames"""
GET_GAS_SOURCES = """
    SELECT *
    FROM GasSources
    WHERE GasType=? AND InUse=True"""
GET_MODULE_SN = """SELECT SensorSN from SensorAssembly Where ModuleSN=?"""
SELECT_SQL = """
SELECT
    *
FROM
    `{}`
WHERE
    SensorSN=?
"""

UPDATE_SQL = """
UPDATE
    `{}`
SET
    CustomBLTable=?, Comment=?
WHERE
    SensorSN=?
"""

INSERT_SQL = """
INSERT INTO
    `{}`(
        SensorType, SensorSN, CustomBLTable, GasTypeID, [Date], Initials, Comment)
VALUES(?,?,?,?,?,?,?)
"""



SELECT_ARCHIVE_RECORD = """
SELECT
    *
FROM
    `{}`
WHERE
    SensorSN=?
"""

GET_RECORD_ID = """
SELECT
    ID
FROM
    `{}`
WHERE
    SensorSN=?
"""

RESTORE_BASELINE = """
UPDATE
    `{}`
SET
    CustomBLTable=?, Comment=?
WHERE
    ID=?
"""