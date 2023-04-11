
from run import Bread, db




db.create_all()

bread1 = Bread("Naminė duona su saulėgrąžomis, moliūgų sėklomis ir kanapių sėklomis ", "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su saulėgrąžomis, moliūgų sėklomis ir kanapių sėklomis, be konservantų", "8.00"),
bread2 = Bread("Naminė duona su saulėgrąžomis ir moliūgų sėklomis", "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su saulėgrąžomis ir moliūgų sėklomis, be konservantų", "7.00"),
bread3 = Bread("Naminė duona su saulėgrąžomis ir kanapių sėklomis",  "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su saulėgražomis ir kanapių sėklomis, be konservantų", "7.00"),
bread4 = Bread("Naminė duona su kmynais",  "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su kmynais, be konservantų", "5.00"),
bread5 = Bread("Naminė duona su saulėgrąžomis",  "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su saulėgrąžomis, be konservantų", "6.00"),
bread6 = Bread("Naminė duona su riešutais ir medumi",  "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su riešutais ir medumi, be konservantų", "6.00"),
bread7 = Bread("Naminė duona su vaisiais",  "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su vaisiais, be konservantų", "7.00")


db.session.add_all([bread1, bread2, bread3, bread4, bread5, bread6, bread7])

db.session.commit()


# INSERT INTO "breads" ("name","description","price") VALUES ("Naminė duona su saulėgrąžomis, moliūgų sėklomis ir kanapių sėklomis", "Ruginių ir kvietinių miltų duona, kepta naudojant natūralų raugą. Duona su saulėgrąžomis, moliūgų sėklomis ir kanapių sėklomis, be konservantų", "8.00")
