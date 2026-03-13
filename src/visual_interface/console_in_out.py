def input_int_bucle(str_request):

    while True:
        print(str_request)
        try: 
            output = int(input())
            return output
        except Exception as e:
            print("Input was no valid because: ",e)

def multiple_input_int_bucle(str_request_list):
    output = []

    for str in str_request_list:
        output.append(input_int_bucle(str))

    return output

def error_output(error):
    print(error)

