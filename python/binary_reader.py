import Group, Person, Gender
import os

FILE = "D:\\fb5swans\\java\\out\\production\\java"
file_list = os.listdir(FILE)


class BinaryReader:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.files = [f for f in os.listdir(self.file_path) if ".bin" in f]
        self.files_loc = [os.path.join(self.file_path, f) for f in self.files]

    def individual_reader(self):
        for file_loc in self.files_loc:
            if os.path.basename(file_loc) == "individualBinary.bin":
                with open(file_loc, "rb") as f:
                    buffer = f.read()
                person = Person.Person.GetRootAs(buffer, 0)
                name = person.Name()
                age = person.Age()
                weight = person.Weight()
                gender = person.Gender()
                return [name.decode("utf-8"), age, weight, gender]

    def group_reader(self):
        for file_loc in self.files_loc:
            if os.path.basename(file_loc) == "groupBinary.bin":
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
                    [person.Name(), person.Age(), person.Weight(), person.Gender()]
                )

            return [
                name.decode("utf-8"),
                age,
                weight,
                [ls[0].decode("utf-8") for ls in people],
            ], people


if __name__ == "__main__":
    obj = BinaryReader(FILE)
    print(obj.individual_reader())
    print(obj.group_reader()[0])
