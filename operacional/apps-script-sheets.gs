// ============================================================
// Google Apps Script — Lista de Espera Emmanuel Duarte
// Cole este código em: script.google.com → Novo projeto
// Depois: Implantar → Novo implantação → Aplicativo Web
// ============================================================

function doPost(e) {
  try {
    var dados = JSON.parse(e.postData.contents);
    var planilha = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

    // Adiciona cabeçalho na primeira vez
    if (planilha.getLastRow() === 0) {
      planilha.appendRow(['Data', 'Nome', 'Email', 'Origem']);
      planilha.getRange(1, 1, 1, 4).setFontWeight('bold');
    }

    // Insere o lead
    planilha.appendRow([
      new Date().toLocaleString('pt-BR', { timeZone: 'America/Sao_Paulo' }),
      dados.nome   || '',
      dados.email  || '',
      dados.origem || 'Site'
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'erro', mensagem: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Permite testar via GET no browser
function doGet(e) {
  return ContentService
    .createTextOutput('Apps Script funcionando ✓')
    .setMimeType(ContentService.MimeType.TEXT);
}
