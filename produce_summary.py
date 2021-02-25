
print("Day 1")
the_file = open("um-deliveries-20140519.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()




print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


def melon_count(day_number, path):
    """Given day number & path to the deliveries, produce report.

    Opens the deliveries file at [path], processes each line, and generates report in all uppercase."""

    print("Day", day_number)
    delivery_log = open(path)

    for line in delivery_log:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        # or you could do this with "list unpacking":
        #
        # melon, count, amount = words

        print(f"Delivered {count} {melon}s for total of ${amount}")
    delivery_log.close()


melon_count(1, "um-deliveries-20140519.txt")
melon_count(2, "um-deliveries-20140520.txt")
melon_count(3, "um-deliveries-20140521.txt")
