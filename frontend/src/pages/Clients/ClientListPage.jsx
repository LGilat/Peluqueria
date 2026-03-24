import { useState, useEffect } from 'react';
import axiosClient from '../../api/axiosClient';

const ClientListPage = () => {
  const [clients, setClients] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    fetchClients();
  }, []);

  const fetchClients = async () => {
    try {
      const response = await axiosClient.get('/cliente/');
      setClients(response.data);
    } catch (error) {
      console.error('Error fetching clients:', error);
    } finally {
      setLoading(false);
    }
  };

  const filteredClients = clients.filter(client =>
    client.nombre.toLowerCase().includes(searchTerm.toLowerCase()) ||
    client.email.toLowerCase().includes(searchTerm.toLowerCase())
  );

  if (loading) {
    return <div className="loading">Cargando clientes...</div>;
  }

  return (
    <div className="clients-page">
      <div className="content-header">
        <h2>Clientes</h2>
        <button className="btn btn-primary">+ Nuevo Cliente</button>
      </div>

      <div className="card">
        <div className="card-header">
          <input
            type="text"
            className="form-input"
            placeholder="Buscar clientes..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{ maxWidth: '300px' }}
          />
        </div>

        <div className="item-list">
          <div style={{ display: 'grid', gridTemplateColumns: '2fr 2fr 1fr 1fr 1fr', padding: '10px 0', borderBottom: '2px solid var(--border-color)', fontWeight: '600', color: '#7f8c8d' }}>
            <span>Nombre</span>
            <span>Email</span>
            <span>Teléfono</span>
            <span>Gasto</span>
            <span>Acciones</span>
          </div>

          {filteredClients.map((client) => (
            <div key={client.id} className="item-row" style={{ display: 'grid', gridTemplateColumns: '2fr 2fr 1fr 1fr 1fr' }}>
              <span style={{ fontWeight: '500' }}>{client.nombre} {client.apellido}</span>
              <span>{client.email}</span>
              <span>{client.telefono}</span>
              <span>${parseFloat(client.gasto_acumulado || 0).toFixed(2)}</span>
              <span>
                <button className="btn btn-secondary" style={{ padding: '4px 8px', fontSize: '0.8rem', marginRight: '5px' }}>Editar</button>
                <button className="btn" style={{ padding: '4px 8px', fontSize: '0.8rem', backgroundColor: '#e74c3c', color: 'white' }}>Eliminar</button>
              </span>
            </div>
          ))}
        </div>

        {filteredClients.length === 0 && (
          <p style={{ padding: '30px', textAlign: 'center', color: '#7f8c8d' }}>
            No se encontraron clientes
          </p>
        )}
      </div>
    </div>
  );
};

export default ClientListPage;
