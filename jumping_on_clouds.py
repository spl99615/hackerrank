def jumpingOnClouds(c):
    jumps = 0
    cloud_arr = c
    no_of_clouds = len(cloud_arr)
    cloud_no = 0
    while cloud_no < no_of_clouds - 1:
        if cloud_no == no_of_clouds - 2:
            jumps += 1
            break
        if cloud_arr[cloud_no + 2] == '0':
            cloud_no = cloud_no + 2
            jumps += 1
            continue
        elif cloud_arr[cloud_no + 1] == '0':
            cloud_no = cloud_no + 1
            jumps += 1
        else:
            cloud_no += 1
    return jumps


if __name__ == '__main__':
    jumps = jumpingOnClouds(list('0 0 0 1 0 0'.split()))
    print(jumps)
