from django.db import connection

class ExcuteSQLQuery:

    @classmethod
    def excute_stored_procedure(cls, sqlStatment, values, many=True):
        """
        this function is used for excuting sql stored procedure
        inputs:
        takes sqlStatment as string
        takes values as tuple 
        many is boolean detrimine if the output have mutliple input set or single outoutset

        output:
        return array of that data backed from stroed procedure
        """

        output = []
        cursor = connection.cursor()

        cursor.execute(sqlStatment, values)
        try:
            if many:
                while cursor.nextset():
                    try:
                        results = cursor.fetchall()
                        if len(results) > 0:
                            output.extend(results)
                        continue
                    except Exception as e:
                        print(e)
                        continue
            else:
                try:
                    results = cursor.fetchall()
                    if len(results) > 0:
                        output.extend(results)
                except Exception as e:
                    print(e)

        finally:
            cursor.close()
            connection.close()
            return output

    @classmethod
    def excute_stored_procedure_returns_final_value_only(cls, sqlStatment, values):
        """
        this function is used for excuting sql stored procedure
        inputs:
        takes sqlStatment as string
        takes values as tuple 
        many is boolean detrimine if the output have mutliple input set or single outoutset

        output:
        return array of that data backed from stroed procedure
        """
        output = None
        cursor = connection.cursor()
        cursor.execute(sqlStatment, values)
        try:
            while cursor.nextset():
                try:
                    results = cursor.fetchall()
                    print(results)
                    if len(results) > 0:
                        output = results
                    continue
                except Exception as e:
                    print(e)
                    continue

        finally:
            cursor.close()
            connection.close()
            return output





