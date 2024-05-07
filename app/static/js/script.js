function confirmDelete(dataID) {
    // Configura o ID do cliente no botão de confirmação no modal
    var confirmBtn = document.getElementById('delete-confirm-btn');
    confirmBtn.onclick = function () {
        deleteData(dataID);
    };

    // Exibe o modal de confirmação
    var confirmModal = new bootstrap.Modal(document.getElementById('confirmDeleteModal'), {
        keyboard: false
    });
    confirmModal.show();
}

function createDataTable(table_name) {
    var objDataTable = new DataTable(table_name, {
        "responsive": true,
        "bJQueryUI": true,
        "autoWidth": false,
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'copy',
                text: 'Copy'
            },
            {
                extend: 'csv',
                text: 'CSV'
            },
            {
                extend: 'excel',
                text: 'Excel'
            },
            {
                extend: 'pdf',
                text: 'PDF'
            },
            {
                extend: 'print',
                text: 'Print'
            }
        ],
        language: {
            // Pt-br
            // url: 'https://cdn.datatables.net/plug-ins/1.11.3/i18n/pt_br.json'
            // En
            url: 'https://cdn.datatables.net/plug-ins/1.11.3/i18n/en-gb.json'
        }
    });

    // Set autoWidth como true
    objDataTable.columns.adjust().draw();

    return objDataTable;
}