function open_update(uid, url, rid) {
    document.getElementById('update_uid').value = uid;
    document.getElementById('update_url').value = url;
    document.getElementById('update_div').style.display = 'block';
    document.getElementById('update_form').action = "/records/update/" + rid;
}

function open_create() {
    document.getElementById('create_div').style.display = "block";
}


function open_del(rid) {
    document.getElementById('del_div').style.display = 'block';
    document.getElementById('del_form').action = "/records/delete/" + rid;
}

function search() {
    uid = document.getElementById('search_input').value;
    url = '/records/detail/' + uid;
    window.location.href=url;
}
