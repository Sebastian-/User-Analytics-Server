"""
A collection of functions used to brute force query calls and investigate the data.

Output from main():

Number of unique users is 8550022
Users using OS 1: 1249619
Users using OS 0 and 6: 1477249
Users using device 3: 767244
Users using device 0 and 5: 1285700
Users using OS 1 and device 1: 6143198
Number of loyal users is 563740
Loyal users using OS 1: 81413
Loyal users using OS 0 and 6: 140467
Loyal users using device 3: 79508
Loyal users using device 0 and 5: 24561
Loyal users using OS 1 and device 1: 414706

"""


users = {}

def main():
    load_data()
    print("Number of unique users is " + str(num_of_unique_users()))
    print("Users using OS 1: " + str(users_with_os(1)))
    print("Users using OS 0 and 6: " + str(users_with_os(0, 6)))
    print("Users using device 3: " + str(users_with_device(3)))
    print("Users using device 0 and 5: " + str(users_with_device(0, 5)))
    print("Users using OS 1 and device 1: " + str(users_combined(1, 1)))
    print("Number of loyal users is " + str(num_of_loyal_users()))
    print("Loyal users using OS 1: " + str(loyal_with_os(1)))
    print("Loyal users using OS 0 and 6: " + str(loyal_with_os(0, 6)))
    print("Loyal users using device 3: " + str(loyal_with_device(3)))
    print("Loyal users using device 0 and 5: " + str(loyal_with_device(0, 5)))
    print("Loyal users using OS 1 and device 1: " + str(loyal_combined(1, 1)))


def num_of_unique_users():
    """Returns the number of unique users"""
    return len(users)


def users_with_os(*args):
    """Returns the number of users using an OS in args"""
    count = 0
    for userInfo in users.values():
        for os in args:
            if os in userInfo['os']:
                count += 1
                break;
    return count


def users_with_device(*args):
    """Returns the number of users using a device in args"""
    count = 0
    for userInfo in users.values():
        for device in args:
            if device in userInfo['device']:
                count += 1
                break;
    return count


def users_combined(os, device):
    """Returns the number of users using both os and device"""
    count = 0
    for userInfo in users.values():
        if os in userInfo['os']:
            count += 1
            continue
        if device in userInfo['device']:
            count += 1
            continue
    return count



def num_of_loyal_users():
    """Returns the number of loyal users"""
    count = 0
    for userInfo in users.values():
        if userInfo['visits'] >= 10:
            count += 1
    return count


def loyal_with_os(*args):
    """Returns the number of loyal users using an OS in args"""
    count = 0
    for userInfo in users.values():
        if userInfo['visits'] < 10:
            continue
        for os in args:
            if os in userInfo['os']:
                count += 1
                break;
    return count


def loyal_with_device(*args):
    """Returns the number of loyal users using a device in args"""
    count = 0
    for userInfo in users.values():
        if userInfo['visits'] < 10:
            continue
        for device in args:
            if device in userInfo['device']:
                count += 1
                break;
    return count


def loyal_combined(os, device):
    """Returns the number of loyal users using both os and device"""
    count = 0
    for userInfo in users.values():
        if userInfo['visits'] < 10:
            continue
        if os in userInfo['os']:
            count += 1
            continue
        if device in userInfo['device']:
            count += 1
            continue
    return count


def load_data():
    """Loads csv data into a dictionary"""
    if users:
        return
    with open('data.csv') as data:
        for line in data:
            userData = line.rstrip('\n').split(',')
            userID = int(userData[1])
            os = int(userData[2])
            device = int(userData[3])

            if userID in users:
                user = users[userID]
                user['os'].add(os)
                user['device'].add(device)
                user['visits'] += 1
            else:
                users[userID] = {
                    'visits': 1,
                    'os': {os},
                    'device': {device}
                    }


# returns false, as expected many users access the site from different devices/os
def has_consistent_user_environment():
    """Checks whether a user always uses the same OS/device"""
    users = {}
    data = open('data.csv')

    for line in data:
        userData = line.split(',')
        if userData[1] in users:
            if users[userData[1]]['os'] != userData[2] or users[userData[1]]['device'] != userData[3]:
                print("User id with differring environment: " + userData[1])
                print("Has os: " + users[userData[1]]['os'] + " and device: " + users[userData[1]]['device'])
                print("Found entry with os: " + userData[3] + " and device: " + userData[3])
                return False
        else:
            users[userData[1]] = {'os': userData[2], 'device': userData[3]}

    return True;


if __name__ == '__main__':
    main()