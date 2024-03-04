import requests
import random

url = "https://x-clients-be.onrender.com"

def test_get_token(user = 'bloom' , password = 'fire-fairy'): 
        creds = { 
        'username' : user, 
        'password' : password 
        } 
        resp = requests.post(url+'/auth/login', json = creds) 
        assert resp.status_code == 201
        return resp.json()["userToken"] 
        


def test_create_new_company(name = 'New Company', description = '8968267891236978263' ):
        company = {
        "name": name,
        "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = test_get_token()
        resp = requests.post(url+'/company', json = company,headers = my_headers)
        assert resp.status_code == 201
        return resp.json()["id"]

def test_get_employee():
        company_id = test_create_new_company()
        params = {'company': company_id}
        resp = requests.get(url + '/employee', params=params)
        assert resp.status_code == 200
        return resp.json()

def test_add_employee(id_employee = None, first_name='Petr', last_name='Ivanov', middle_name='Ivanovich', id_company=None, mail='datch@example.com', employee_url='http://www.google.com', phone='8976493208', birthdate='2024-02-22T08:24:56.028Z'):
    if id_employee is None:
        id_employee = random.randint(1, 1000)
    if id_company is None:
        id_company = test_create_new_company()
    if not all([first_name, last_name, id_company, mail, phone, birthdate]):
        raise ValueError("Не все обязательные поля заполнены")
    add_employee = {
        "id": id_employee,
        "firstName": first_name,
        "lastName": last_name,
        "middleName": middle_name,
        "companyId": id_company,
        "email": mail,
        "url": employee_url,
        "phone": phone,
        "birthdate": birthdate,
        "isActive": True
    }
    my_headers = {}
    my_headers["x-client-token"] = test_get_token()
    resp = requests.post(url+'/employee', json=add_employee, headers=my_headers)
    assert resp.status_code == 201
    return resp.json()
def test_id_employee():
    id = test_add_employee()
    params = id  
    resp = requests.get(url+'/employee', params = params)
    print(id)
    assert resp.status_code == 200
    return resp.json()

def test_change_employee(change_lastName = "Petr", change_email = "313123@mail.ru", change_url = "https://ya.ru/", change_phone = "8976493208", change_active = "False"):
    change_employee = {
  "lastName": change_lastName,
  "email": change_email,
  "url": change_url,
  "phone": change_phone,
  "isActive": change_active
}
    my_headers = {}
    my_headers["x-client-token"] = test_get_token()
    resp = requests.patch(url+'/employee', json=change_employee, headers=my_headers)
    return resp.json()