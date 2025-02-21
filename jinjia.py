@app.route("profile/",method=['GET'])
def profile(username=None):
    username = request.args.get('username')
    with open("profile.html") as f:
        jinjia2.Template(f.read()).render(username=username)
