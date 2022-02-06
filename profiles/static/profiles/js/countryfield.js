let countrySelected = $('#id_country').val();
if(!countrySelected) {
    $('#id_country').css('color', '#819c88');
};
$('#id_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#819c88');
    } else {
        $(this).css('color', '#0f5520')
    }
});