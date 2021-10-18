# Problem Statement : https://www.geeksforgeeks.org/allocate-minimum-number-pages/

# Method to check that whether it is possible to allocate given students with given page limit.
def isPossible(arr,n,students,limit):

    curr_students = 1
    curr_sum = 0

    # Iterate over all the books.
    for i in range(n):

        # If the pages in the current books is greater than the limit than it is not possible to allocate pages with limit.
        if arr[i] > limit:
            return False

        # Check how many students are required to distribute curr_ minimum pages.
        if curr_sum + arr[i] > limit:
            # if adding pages of curr book is getting beyond the limit than assign it to new book so increase the student count by 1 and assign
            # him pages of the current book.
            curr_students += 1
            curr_sum = arr[i]

            # If at any steps student count becomes greater than given students in question than return false as we are not able to allocate pages
            # to given number of students  by limiting to the given pages.
            if curr_students > students:
                return False

        else:
            curr_sum += arr[i]   # Increase page count of the current students.

    # Return true this means we are able to allocate books between given students by keeping given page limit for each students.
    return True

# TC = O(N)
# SC = O(1)
def findMinimumPages(arr,n,students):

    # Base case , If number of students are greater than number of books than it is impossible to allocate books to all students.
    if students > n:
        return -1

    books_sum = 0

    # Take Sum of all the pages in the books
    for book in arr:
        books_sum += book

    # Set limits for binary search.
    start,end = arr[0] , books_sum
    result = 10000000


    # Now Apply Binary search in the start to end search space.
    while start <= end:

        mid = (start+end) // 2

        # If it is possible to allocate books to given students by keeping mid page limit for each students the store the result and
        # make high = mid - 1 as we care looking for minimum gap so it will lie in left side of search space.
        if isPossible(arr,n,students,mid):
            result = mid
            end = mid - 1

        # Else  increase the page limit.
        else:
            start = mid + 1

    # Once the Binary search is done than return the result.
    return result



# Driver Code
arr = [15,17,20]
students = 2
print("Minimum Number of pages {}".format(findMinimumPages(arr,len(arr),students)))