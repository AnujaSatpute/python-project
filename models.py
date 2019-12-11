import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('functions\\tourdo.db')
        #self.create_user_table()
        self.create_tour_do_table()
        # Why are we calling user table before tour_do table
        # what happens if we swap them?

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_tour_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Tourdo" (
          "cid" INTEGER PRIMARY KEY,
          "cname" TEXT,
          "packagename" TEXT,
          "destination" TEXT,
          "_is_deleted" boolean DEFAULT 0
        );

        """

        self.conn.execute(query)
#Schema Ends


class TourDoModel:
   

    def __init__(self):
        self.conn = sqlite3.connect('functions\\tourdo.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def list_items(self, where_clause=""):
        query='''select * from Tourdo where _is_deleted != 1'''+where_clause
        #print (query)
        cur = self.conn.cursor()
        cur.execute(query)
        result_set = cur.fetchall()
        return result_set

    def sql_edit_insert(self,var):
        #print(var)
        query='''insert into Tourdo(cname,packagename,destination) values (?,?,?)'''
        cur = self.conn.cursor()
        cur.execute(query,var)
        self.conn.commit()
        
    def sql_delete(self,ID):
        print("Inside sql_delete",ID)
        print("Type",type(ID))
        query='''UPDATE Tourdo SET _is_deleted=1 where cid=?'''
        print("Query",query)
        cur = self.conn.cursor()
        cur.execute(query,ID)
        self.conn.commit()  

    def sql_edit(self,var):
        query='''UPDATE Tourdo SET cname= ?,packagename= ?,destination =? where cid=?'''
        cur = self.conn.cursor()
        print("*"*8)
        print(var)
        cur.execute(query,var)
        self.conn.commit()      
    

#end TourDoModel
