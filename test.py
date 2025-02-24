import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyODIwOTU5LCJpYXQiOjE3NDAyMjg5NTksImp0aSI6ImRmNDI1Mjk0ODY3NjQ1ODU5YzFkODI4OGU4ZWYzZjE1IiwidXNlcl9pZCI6NjZ9.XNX1jqf-yMzdrRw15ha0Q8JRggql5i4RaxYrl4kxwRA',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'http://localhost:5173',
    'Referer': 'http://localhost:5173/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Storage-Access': 'active',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36 Edg/133.0.0.0',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

params = {
    'branch_id': '1',
    'academic_year_id': '2',
}

json_data = [
    {
        'attendance_data': [
            {
                'attendance_id': 224924,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 240766,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253387,
                'status': '5',
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224936,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 240778,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253399,
                'status': '5',
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224929,
                'status': 4,
                'comment': '.',
            },
            {
                'attendance_id': 240771,
                'status': 0,
                'comment': '.',
            },
            {
                'attendance_id': 253392,
                'status': '5',
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224931,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 240773,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253394,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224940,
                'status': 4,
                'comment': '.',
            },
            {
                'attendance_id': 240782,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253403,
                'status': '5',
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224941,
                'status': 4,
                'comment': '.',
            },
            {
                'attendance_id': 240783,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 253404,
                'status': '4',
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {},
            {
                'attendance_id': 240785,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253406,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224922,
                'status': 4,
                'comment': '.',
            },
            {
                'attendance_id': 240764,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253385,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224938,
                'status': 4,
                'comment': '.',
            },
            {
                'attendance_id': 240780,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253401,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224930,
                'status': 4,
                'comment': '.',
            },
            {
                'attendance_id': 240772,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 253393,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224927,
                'status': 4,
                'comment': '.',
            },
            {
                'attendance_id': 240769,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253390,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224928,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 240770,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253391,
                'status': '5',
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224942,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 240784,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 253405,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224926,
                'status': 3,
                'comment': '.',
            },
            {
                'attendance_id': 240768,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253389,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224925,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 240767,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253388,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224935,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 240777,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 253398,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224933,
                'status': 4,
                'comment': '.',
            },
            {
                'attendance_id': 240775,
                'status': 4,
                'comment': '.',
            },
            {
                'attendance_id': 253396,
                'status': '5',
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224939,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 240781,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253402,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224937,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 240779,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 253400,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224932,
                'status': 4,
                'comment': '.',
            },
            {
                'attendance_id': 240774,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253395,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224923,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 240765,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 253386,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {},
            {
                'attendance_id': 240786,
                'status': 1,
                'comment': '.',
            },
            {
                'attendance_id': 253407,
                'status': -1,
                'comment': '.',
            },
        ],
    },
    {
        'attendance_data': [
            {
                'attendance_id': 224934,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 240776,
                'status': 5,
                'comment': '.',
            },
            {
                'attendance_id': 253397,
                'status': -1,
                'comment': '.',
            },
        ],
    },
]
for i in range(100):
    response = requests.post('http://127.0.0.1:8000/api/v1/attendance/update/', params=params, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '[{"attendance_data":[{"attendance_id":224924,"status":5,"comment":"."},{"attendance_id":240766,"status":1,"comment":"."},{"attendance_id":253387,"status":"5","comment":"."}]},{"attendance_data":[{"attendance_id":224936,"status":1,"comment":"."},{"attendance_id":240778,"status":1,"comment":"."},{"attendance_id":253399,"status":"5","comment":"."}]},{"attendance_data":[{"attendance_id":224929,"status":4,"comment":"."},{"attendance_id":240771,"status":0,"comment":"."},{"attendance_id":253392,"status":"5","comment":"."}]},{"attendance_data":[{"attendance_id":224931,"status":5,"comment":"."},{"attendance_id":240773,"status":1,"comment":"."},{"attendance_id":253394,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224940,"status":4,"comment":"."},{"attendance_id":240782,"status":1,"comment":"."},{"attendance_id":253403,"status":"5","comment":"."}]},{"attendance_data":[{"attendance_id":224941,"status":4,"comment":"."},{"attendance_id":240783,"status":5,"comment":"."},{"attendance_id":253404,"status":"4","comment":"."}]},{"attendance_data":[{},{"attendance_id":240785,"status":1,"comment":"."},{"attendance_id":253406,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224922,"status":4,"comment":"."},{"attendance_id":240764,"status":1,"comment":"."},{"attendance_id":253385,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224938,"status":4,"comment":"."},{"attendance_id":240780,"status":1,"comment":"."},{"attendance_id":253401,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224930,"status":4,"comment":"."},{"attendance_id":240772,"status":5,"comment":"."},{"attendance_id":253393,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224927,"status":4,"comment":"."},{"attendance_id":240769,"status":1,"comment":"."},{"attendance_id":253390,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224928,"status":5,"comment":"."},{"attendance_id":240770,"status":1,"comment":"."},{"attendance_id":253391,"status":"5","comment":"."}]},{"attendance_data":[{"attendance_id":224942,"status":5,"comment":"."},{"attendance_id":240784,"status":5,"comment":"."},{"attendance_id":253405,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224926,"status":3,"comment":"."},{"attendance_id":240768,"status":1,"comment":"."},{"attendance_id":253389,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224925,"status":5,"comment":"."},{"attendance_id":240767,"status":1,"comment":"."},{"attendance_id":253388,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224935,"status":5,"comment":"."},{"attendance_id":240777,"status":5,"comment":"."},{"attendance_id":253398,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224933,"status":4,"comment":"."},{"attendance_id":240775,"status":4,"comment":"."},{"attendance_id":253396,"status":"5","comment":"."}]},{"attendance_data":[{"attendance_id":224939,"status":5,"comment":"."},{"attendance_id":240781,"status":1,"comment":"."},{"attendance_id":253402,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224937,"status":5,"comment":"."},{"attendance_id":240779,"status":5,"comment":"."},{"attendance_id":253400,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224932,"status":4,"comment":"."},{"attendance_id":240774,"status":1,"comment":"."},{"attendance_id":253395,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224923,"status":5,"comment":"."},{"attendance_id":240765,"status":5,"comment":"."},{"attendance_id":253386,"status":-1,"comment":"."}]},{"attendance_data":[{},{"attendance_id":240786,"status":1,"comment":"."},{"attendance_id":253407,"status":-1,"comment":"."}]},{"attendance_data":[{"attendance_id":224934,"status":5,"comment":"."},{"attendance_id":240776,"status":5,"comment":"."},{"attendance_id":253397,"status":-1,"comment":"."}]}]'
#response = requests.post('http://127.0.0.1:8000/api/v1/attendance/update/', params=params, headers=headers, data=data)