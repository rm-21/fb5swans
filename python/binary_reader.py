import Group, Person, Gender
import os

FILE = "D:\\fb5swans\\java\\out\\production\\java"
file_list = os.listdir(FILE)


class BinaryReader:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.files = [f for f in os.listdir(self.file_path) if ".bin" in f]
        self.files_loc = [os.path.join(self.file_path, f) for f in self.files]

    def reader(self):
        for file_loc in self.files_loc:
            with open(file_loc, "rb") as f:
                buffer = f.read()
            type = Person.Person.GetRootAs(buffer, 0)
            if type.Group():
                print(self.group_reader(file_loc), end="\n")
            if not type.Group():
                print(self.individual_reader(file_loc), end="\n")

    def individual_reader(self, file_loc):
        with open(file_loc, "rb") as f:
            buffer = f.read()
        person = Person.Person.GetRootAs(buffer, 0)
        name = person.Name()
        age = person.Age()
        weight = person.Weight()
        gender = person.Gender()
        return [name.decode("utf-8"), age, weight, gender]

    def group_reader(self, file_loc):
        with open(file_loc, "rb") as f:
            buffer = f.read()

        group = Group.Group.GetRootAs(buffer, 0)

        name = group.Name()
        age = group.Age()
        weight = group.Weight()
        people = []

        for i in range(group.PeopleLength()):
            person = group.People(i)
            people.append(
                [
                    person.Name().decode("utf-8"),
                    person.Age(),
                    person.Weight(),
                    person.Gender(),
                ]
            )

        return [
            name.decode("utf-8"),
            age,
            weight,
            [ls[0] for ls in people],
        ], people


if __name__ == "__main__":
    obj = BinaryReader(FILE)
    obj.reader()
