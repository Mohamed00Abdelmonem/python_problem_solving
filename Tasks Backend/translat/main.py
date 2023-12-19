# world_user = input("Enter your world: ")
# world_do_not_using = ["a", "i", "o", "u", "e"]
# world_finshed = ""
# for counter in world_user:
#
#     if counter == "a" or counter == "i" or counter == "u" or counter == "e" or counter == "o":
#         world_finshed += "$"
#
#     else:
#         world_finshed += counter
#
# print(world_finshed)
#


def translate(input):
    world_fished = ""

    for latter in input:
        if latter.lower() in "auieo":
            world_fished += "z"

        else:
            world_fished += latter

    print(world_fished)


translate((input("Enter your word: ")))

print()
