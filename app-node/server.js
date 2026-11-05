const http = require('http');
const PORT = 5000;

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('¡Servidor Node.js activo!');
});

server.listen(PORT, () => {
    console.log(`Servidor ejecutándose en el puerto ${PORT}`);
});