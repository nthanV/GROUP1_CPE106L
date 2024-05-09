BEGIn TRANSACTION;

-- Ensure the table "ADVENTURE_TRIP" exists or create it if not
CREATE TABLE IF NOT EXISTS "ADVENTURE_TRIP" (
    "TRIP_ID" DECIMAL,
    "TRIP_NAME" VARCHAR(75),
    "START_LOCATION" CHAR(50),
    "STATE" CHAR(2),
    "DISTANCE" NUMBER(10, 2),
    "MAX_GRP_SIZE" NUMBER(10, 2),
    "TYPE" CHAR(20),
    "SEASON" CHAR(20)
);

-- Insert data into the "ADVENTURE_TRIP" table
INSERT INTO "ADVENTURE_TRIP" VALUES (45, 'Jaye Peak', 'Jay', 'VT', 8, 8, 'Hiking', 'Summer');

-- Commit the transaction to save the changes
COMMIT;
