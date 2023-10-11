from main import app

def test_home_route():
    response=app.test_client().get('/')
    assert response.status_code == 200
    assert b'<h1>Home page</h1>' in response.data
    assert b'<h2>This is Evise from  Hometown </h2>' in response.data
    assert b'<span>number of views = 123</span>' in response.data

def test_user_path_route_2args():
    response=app.test_client().get('/user/Dan/Texas')
    assert response.status_code == 200
    assert b'h1>User Dan profile</h1>' in response.data
    assert b'<h2>Home city is Texas</h2>' in response.data


def test_user_path_route_1arg():
    response=app.test_client().get('/user/Dan')
    assert response.status_code == 200
    assert b'h1>User Dan profile</h1>' in response.data


def test_user_query_2args():
    response=app.test_client().get('/user?name=Dan&city=Texas')
    assert response.status_code == 200
    assert b'h1>User Dan profile</h1>' in response.data
    assert b'<h2>Home city is Texas</h2>' in response.data


def test_user_query_1args():
    response=app.test_client().get('/user?name=Dan')
    assert response.status_code == 200
    assert b'h1>User Dan profile</h1>' in response.data