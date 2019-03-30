import pickle
from sqlite3 import dbapi2 as sqlite

class Indexer(object):
    def __init__(self,db,voc):
        self.con = sqlite.connect(db)
        self.voc = voc

    def __del__(self):
        self.con.close()

    def db_commit(self):
        self.con.commit()


class Searcher(object):
    def __init__(self,db,voc):
        self.con = sqlite.connect(db)
        self.voc=voc

    def __del__(self):
        self.con.close()

    def candidates_from_word(self,imword):
        im_ids = self.con.execute(
            "select distinct imid from imwords where wordid=%d" % imword
        ).fetchall()
        return [i[0] for i in im_ids]
