import time

class ListMaker:
    def __init__(self):
        self.lists = []

    def create_list(self):
        name = input("\nName the List: ").upper()
        num_items = int(input("\nEnter number of items: "))
        items = []
        deleted_items = []

        def add_to_list():
            while len(items) < num_items:
                new_item = input(f"\nAdd new item to {name} : ").upper()
                if new_item not in items:
                    items.append(new_item)
                    items.sort()
                    time.sleep(0.5)
                    print(f"\nList Count: [{len(items)}], Left with [{num_items - len(items)}]")
                    print(", ".join(items))
                else:
                    print(f"{new_item} already exists on {name} list")

        add_to_list()

        def delete_items():
            while True:
                item_to_delete = input("\nItem to delete: ").upper()
                if item_to_delete in items:
                    items.remove(item_to_delete)
                    deleted_items.append(item_to_delete)
                    print(f"\n{item_to_delete} deleted from {name} list successfully!!")
                    print(f"\nList Count: [{len(items)}], Left with [{num_items - len(items)}]")
                    print(", ".join(items))
                else:
                    while item_to_delete not in items:
                        item_to_delete = input(f"\nTRY AGAIN !! {item_to_delete} not on {name} List!!\nItem to delete: ").upper()
                    items.remove(item_to_delete)
                    deleted_items.append(item_to_delete)
                    print(f"\n{item_to_delete} deleted from {name} list successfully!!")
                    print(f"\nList Count: [{len(items)}], Left with [{num_items - len(items)}]")
                    print(", ".join(items))
                choice = input("\nContinue Editing?\n[Y/N]?? : ").lower()
                while choice not in ["y", "n"]:
                    print("try again")
                    choice = input("\nContinue Editing?\n[Y/N]?? : ").lower()
                if choice == "n":
                    break

        edit_choice = input(f"\nDo you need to [DELETE] any item in the {name} list above? [ Y /N ]?? : ").lower()
        if edit_choice == "y":
            delete_items()

        add_more = input("Replace Deleted Items? [ Y / N ]?? : ").lower()
        if add_more == "y":
            add_to_list()

        time.sleep(5)
        print(f"\nCollected the {len(items)} items on the {name} list below:\n")
        print(f"{name} List:")
        for index, char in enumerate(items):
            print(f"{index+1} - {char}")
        print()

        print(f"\nDeleted the {len(deleted_items)} items from the {name} list above:\n")
        print(f"Deleted items List:")
        for index, char in enumerate(deleted_items):
            print(f"{index+1} - {char}")
        print()

def main():
    num_lists = 0
    while True:
        if num_lists == 0:
            print("\nWELCOME TO THE LIST MAKER!!")
            list_maker = ListMaker()
            list_maker.create_list()
            num_lists += 1
        else:
            num_lists += 1
            choice = input("DO YOU WANT TO MAKE ANOTHER LIST?\n[Y/N]?? : ").lower()
            while choice not in ["y", "n"]:
                print("try again")
                choice = input("DO YOU WANT TO MAKE ANOTHER LIST?\n[Y/N]?? : ").lower()
            if choice == "n":
                print(f"\nYOU HAVE USED LIST MAKER TO MAKE [{num_lists}] LISTS!!\n")
                break
            else:
                list_maker = ListMaker()
                list_maker.create_list()

if __name__ == "__main__":
    main()
