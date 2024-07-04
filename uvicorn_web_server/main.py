async def app(scope, receive, send):
    # assert used for debug
    # if scope type == http, it does not debug anything
    # scope, receive, send (everything are dictionary)

    assert scope["type"] == "http"

    try:
        # header
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/plain"],
            ]
        })
        

        # body
        await send({
            "type": "http.response.body",
            "body": b"Hello, World!",
        })
    
    except Exception as e:
        print("Failed to start server:", e)

