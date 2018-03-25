function open_update(uid, url, rid) {
    document.getElementById('update_uid').value = uid;
    document.getElementById('update_url').value = url;
    document.getElementById('update_bg').style.display = 'block';
    document.getElementById('update_form').action = "/records/update/" + rid;
}

function open_create() {
    document.getElementById('create_bg').style.display = "block";
}


function open_del(rid) {
    document.getElementById('del_bg').style.display = 'block';
    document.getElementById('del_form').action = "/records/delete/" + rid;
}

function search() {
    var uid = document.getElementById('search_input').value;
    var url = '/records/list/';
    if (uid == null) {
        url = url + '?uid=' + uid;
    }
    window.location.href=url;
}

function hide_bg() {
    var bgs = document.getElementsByClassName('bg_div');
    for(var i=0;i<bgs.length;i++) {
       bgs[i].style.display = 'none';
    }
}