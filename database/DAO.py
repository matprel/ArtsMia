from database.DB_connect import DBConnect
from model.arco import Arco
from model.oggetto import Oggetto


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllOggetti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM objects"

        cursor.execute(query)

        for row in cursor:
            result.append(Oggetto(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select eo1.object_id, eo2.object_id, count(*) as peso
                    from exhibition_objects eo1, exhibition_objects eo2
                    where eo1.exhibition_id = eo2.exhibition_id and eo1.object_id != eo2.object_id
                    group by eo1.object_id, eo2.object_id """

        cursor.execute(query)

        for row in cursor:
            result.append(Arco(idMap[row["object_id"]], idMap[row["object_id"]], row["peso"]))

        cursor.close()
        conn.close()
        return result
