
BEGIN TRANSACTION;
CREATE TABLE "Participants" (
	"ParticipantsNumber" INTEGER PRIMARY KEY,
	"LastName"	TEXT,
	"FirstName"	TEXT,
	"Address"	TEXT,
	"City"	TEXT,
	"State"	TEXT,
	"PostalCode"	TEXT,
	"Telephone"	TEXT,
	"BirthDate"	INTEGER)
);
CREATE TABLE "Adventure Class" (
	"ClassNumber"	INTEGER PRIMARY KEY,
	"ClassDescription"	TEXT,
	"MaxNumOfParticipants"	INTEGER,
	"InstructorId"	INTEGER PRIMARY KEY,
	"ClassFee"	NUMERIC)
);
CREATE TABLE "Enrolled Participants" (
	"ParticipantNumber"	INTEGER PRIMARY KEY,
	"LastName"	TEXT,
	"FirstName"	TEXT,
	"ClassNumber"	INTEGER PRIMARY KEY,
	"ClassDescription"	TEXT,
	"DateOfClass"	INTEGER)
);
CREATE TABLE "Class" (
	"ClassDate"	INTEGER,
	"ClassNumber"	INTEGER PRIMARY KEY,
	"ClassDescription"	TEXT,
	"ParticipantNumber"	INTEGER PRIMARY KEY,
	"LastName"	TEXT,
	"FirstName"	TEXT)
);
COMMIT;