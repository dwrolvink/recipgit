
// Triggers
// -------------------------------------
function onclick_block(el){
    if (el.enabled != 'true'){
        block_enable(el)
    }
    else {
        block_disable(el)
    }
}

// Main functions
// -------------------------------------
function block_enable(el){
    el.enabled = 'true'
    block_say_hi(el)
    call_block_loadBgColor(el)
}

function block_disable(el){
    el.enabled = 'false'
    el.style.backgroundColor = ''
    el.innerHTML = '&nbsp;'
}

// Secondary functions
// -------------------------------------
function block_say_hi(element){
    element.innerHTML = "hello";
}
function call_block_loadBgColor(el){
    httpGetJsonAsync(url='/api/v1/background_color', callback=[block_loadBgColor, el])
}
function block_loadBgColor(response, el){
    el.style.backgroundColor = response.bg_color;
}

