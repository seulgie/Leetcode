class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert the input 'num' to a list of character 'arr'
        arr = list(str(num))

        # Iterate over the list
        for i, num in enumerate(arr):
            if num == '6':
                arr[i] = '9'
                break

        # Convert the modified arr to integer and return it.
        return int("".join(arr))
        
