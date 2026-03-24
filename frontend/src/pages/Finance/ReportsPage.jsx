import { useEffect, useState } from 'react';
import axiosClient from '../../api/axiosClient';

const ReportsPage = () => {
  const [data, setData] = useState([]);
  const [year, setYear] = useState(new Date().getFullYear());
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchReports();
  }, [year]);

  const fetchReports = async () => {
    try {
      setLoading(true);
      const response = await axiosClient.get(`/reportes-financieros/?year=${year}`);
      setData(response.data.data || []);
    } catch (error) {
      console.error('Error fetching reports:', error);
    } finally {
      setLoading(false);
    }
  };

  const maxValue = Math.max(
    1,
    ...data.map((row) => Math.max(row.ingresos || 0, row.gastos || 0))
  );

  if (loading) {
    return <div className="loading">Cargando reportes...</div>;
  }

  return (
    <div className="reports-page">
      <div className="content-header">
        <h2>Reportes Financieros</h2>
        <input
          type="number"
          className="form-input"
          value={year}
          onChange={(e) => setYear(e.target.value)}
          style={{ maxWidth: '120px' }}
        />
      </div>

      <div className="card">
        <div className="item-list">
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr 1fr 1fr 2fr', padding: '10px 0', borderBottom: '2px solid var(--border-color)', fontWeight: '600', color: '#7f8c8d' }}>
            <span>Mes</span>
            <span>Ingresos</span>
            <span>Gastos</span>
            <span>Margen</span>
            <span>Servicios</span>
            <span>Productos</span>
            <span>Gráfico</span>
          </div>
          {data.length === 0 ? (
            <p style={{ padding: '20px', color: '#7f8c8d' }}>Sin datos.</p>
          ) : (
            data.map((row) => (
              <div key={`${row.year}-${row.month}`} className="item-row" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr 1fr 1fr 2fr', alignItems: 'center' }}>
                <span>{row.month}/{row.year}</span>
                <span>${parseFloat(row.ingresos).toFixed(2)}</span>
                <span>${parseFloat(row.gastos).toFixed(2)}</span>
                <span>${parseFloat(row.margen).toFixed(2)}</span>
                <span>${parseFloat(row.ingresos_servicios).toFixed(2)}</span>
                <span>${parseFloat(row.ingresos_productos).toFixed(2)}</span>
                <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
                  <div
                    title={`Ingresos: ${row.ingresos}`}
                    style={{
                      height: '10px',
                      width: `${(row.ingresos / maxValue) * 100}%`,
                      background: '#27ae60',
                      borderRadius: '6px'
                    }}
                  />
                  <div
                    title={`Gastos: ${row.gastos}`}
                    style={{
                      height: '10px',
                      width: `${(row.gastos / maxValue) * 100}%`,
                      background: '#e74c3c',
                      borderRadius: '6px'
                    }}
                  />
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};

export default ReportsPage;
