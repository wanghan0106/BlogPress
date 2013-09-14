var bootstrap_validtion={};

$(function(){
    $('form').each(function() {
        bootstrap_validtion.load(form);
        $(this).bind('submit',function(){
            return bootstrap_validtion.validate(this);
        });
    });
});
bootstrap_validtion.load = function(form) {
    var validator = {}
    validator.elements = [];
    validator.elements = validator.elements.concat($('input').not($('input[type="hidden"]')));
    validator.elements = validator.elements.concat($('textarea'));
    $(this).data('validator',validator);
}
bootstrap_validtion.validate = function(form) {
    var validator = $(this).data('validator');
    if(!validator || !validator.elements) {
        return true;
    }
    var length = validator.elements.length;
    var valid = true;
    for(var i=0;i<length;i++) {
        var elementValid = true;
        var required = $(this).attr('required');
        var display = $(this).css('display');
        if(display==false) {
            continue;
        }
        if(required) {
            var value = $(this).val();
            if(value && value.length>0) {
                elementValid = true;
            } else {
                var text = $(this).text();
                if(text && text.length>0) {
                    elementValid = true;
                }
                elementValid = false;
                valid = false;
            }
        }
        if(elementValid) {
            $(this).parent().parent().addClass("has-error");
        } else {
            $(this).parent().parent().removeClass("has-error");
        }
    }
    return valid;
}


