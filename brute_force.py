"""
A collection of functions used to brute force query calls and investigate the data.

Output from main():

Number of unique users is 8550022
Users using OS 1: 1249619
Users using OS 0 and 6: 1477249
Users using device 3: 767244
Users using device 0 and 5: 1285700

"""


users = {}

def main():
    load_data()
    print("Number of unique users is " + str(num_of_unique_users()))
    print("Users using OS 1: " + str(users_with_os(1)))
    print("Users using OS 0 and 6: " + str(users_with_os(0, 6)))
    print("Users using device 3: " + str(users_with_device(3)))
    print("Users using device 0 and 5: " + str(users_with_device(0, 5)))


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


def num_of_unique_users():
    """Returns the number of unique users"""
    load_data()
    return len(users)


if __name__ == '__main__':
    main()