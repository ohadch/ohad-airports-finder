from server.services.db import Database


class QueryManager:

    def __init__(self, db: Database):
        self.db = db

    @classmethod
    def from_default_db(cls):
        db = Database.from_default_path()
        return cls(db)

    def get_airports_by_us_state_and_runway(self, us_state: str, runway: int):
        other_runway = runway - 18 if runway > 18 else runway + 18
        runways = ", ".join([f"'{str(runway).zfill(2)}'", f"'{str(other_runway).zfill(2)}'"])
        print(f"Filtering by state: {us_state} and runways {runways}")

        q = f"""
        WITH rel_airports AS (
            SELECT
                *
            FROM 
                airports
            WHERE 
                iso_region = "{us_state}"
        ),
        rel_runways AS (
            SELECT
                airport_ident
            FROM 
                runways
            WHERE 
                he_ident IN ({runways}) OR le_ident IN ({runways})
        )

        SELECT
            rel_airports.ident,
            rel_airports.latitude_deg,
            rel_airports.longitude_deg
        FROM rel_airports
        JOIN rel_runways
            ON rel_airports.ident = rel_runways.airport_ident
        """

        return self.db.fetch(q)
