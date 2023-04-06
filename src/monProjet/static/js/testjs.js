$(document).ready(function() {
    // Fonction de gestion de l'événement "drop"
    $("#dropzone").on("drop", function(event) {
        // Empêche le comportement par défaut de la zone de drop
        event.preventDefault();
        // Récupère le fichier envoyé
        var file = event.originalEvent.dataTransfer.files[0];
        // Envoie le fichier au serveur
        var formData = new FormData();
        formData.append('file', file);
        $.ajax({
            type: 'POST',
            url: '/upload/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                alert("Fichier uploadé avec succès !");
            },
            error: function(error) {
                alert("Erreur lors de l'upload du fichier.");
            }
        });
    });
    // Empêche le comportement par défaut des événements "dragover" et "dragenter"
    $("#dropzone").on("dragover dragenter", function(event) {
        event.preventDefault();
    });
    // Restaure le style par défaut de la zone de drop lors de l'événement "dragleave"
    $("#dropzone").on("dragleave", function(event) {
        $(this).removeClass("dragover");
    });
});