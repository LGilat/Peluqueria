import { useEffect, useMemo, useState } from 'react';
import axiosClient from '../../api/axiosClient';

const ReportsPage = () => {
  const [data, setData] = useState([]);
  const [ingresos, setIngresos] = useState([]);
  const [gastos, setGastos] = useState([]);
  const [year, setYear] = useState(new Date().getFullYear());
  const [month, setMonth] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchReports();
  }, [year]);

  const fetchReports = async () => {
    try {
      setLoading(true);
      const [resReport, resIngresos, resGastos] = await Promise.all([
        axiosClient.get(`/reportes-financieros/?year=${year}`),
        axiosClient.get('/ingreso/'),
        axiosClient.get('/gasto/')
      ]);
      setData(resReport.data.data || []);
      setIngresos(resIngresos.data || []);
      setGastos(resGastos.data || []);
    } catch (error) {
      console.error('Error fetching reports:', error);
    } finally {
      setLoading(false);
    }
  };

  const ingresosFiltrados = useMemo(() => {
    return ingresos.filter((i) => {
      const d = new Date(i.fecha);
      if (d.getFullYear() !== Number(year)) return false;
      if (month && d.getMonth() + 1 !== Number(month)) return false;
      return true;
    });
  }, [ingresos, year, month]);

  const gastosFiltrados = useMemo(() => {
    return gastos.filter((g) => {
      const d = new Date(g.fecha);
      if (d.getFullYear() !== Number(year)) return false;
      if (month && d.getMonth() + 1 !== Number(month)) return false;
      return true;
    });
  }, [gastos, year, month]);

  const totalIngresos = ingresosFiltrados.reduce((sum, i) => sum + parseFloat(i.cantidad), 0);
  const totalGastos = gastosFiltrados.reduce((sum, g) => sum + parseFloat(g.cantidad), 0);
  const balance = totalIngresos - totalGastos;

  if (loading) {
    return <div className="loading">Cargando reportes...</div>;
  }

  return (
    <div className="reports-page">
      <div className="content-header">
        <h2>Finanzas</h2>
        <div style={{ display: 'flex', gap: '8px' }}>
          <input
            type="number"
            className="form-input"
            value={year}
            onChange={(e) => setYear(e.target.value)}
            style={{ maxWidth: '120px' }}
          />
          <select
            className="form-input"
            value={month}
            onChange={(e) => setMonth(e.target.value)}
            style={{ maxWidth: '140px' }}
          >
            <option value="">Mes (todos)</option>
            {Array.from({ length: 12 }, (_, i) => i + 1).map((m) => (
              <option key={m} value={m}>{m}</option>
            ))}
          </select>
        </div>
      </div>

      <div className="card">
        <div className="item-list">
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', padding: '10px 0', borderBottom: '2px solid var(--border-color)', fontWeight: '600', color: '#7f8c8d' }}>
            <span>Mes</span>
            <span>Ingresos</span>
            <span>Gastos</span>
            <span>Margen</span>
          </div>
          {data.length === 0 ? (
            <p style={{ padding: '20px', color: '#7f8c8d' }}>Sin datos.</p>
          ) : (
            data.map((row) => (
              <div key={`${row.year}-${row.month}`} className="item-row" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr' }}>
                <span>{row.month}/{row.year}</span>
                <span>${parseFloat(row.ingresos).toFixed(2)}</span>
                <span>${parseFloat(row.gastos).toFixed(2)}</span>
                <span>${parseFloat(row.margen).toFixed(2)}</span>
              </div>
            ))
          )}
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px', marginTop: '16px' }}>
        <div className="card">
          <div className="card-header"><strong>Ingresos (detalle)</strong></div>
          <div className="item-list">
            <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', padding: '10px 0', borderBottom: '2px solid var(--border-color)', fontWeight: '600', color: '#7f8c8d' }}>
              <span>Concepto</span>
              <span>Importe</span>
            </div>
            {ingresosFiltrados.map((i) => (
              <div key={`ing-${i.id}`} className="item-row" style={{ display: 'grid', gridTemplateColumns: '2fr 1fr' }}>
                <span>{i.tipo}</span>
                <span>${parseFloat(i.cantidad).toFixed(2)}</span>
              </div>
            ))}
            {ingresosFiltrados.length === 0 && (
              <p style={{ padding: '20px', color: '#7f8c8d' }}>Sin ingresos.</p>
            )}
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', borderTop: '1px solid var(--border-color)', paddingTop: '10px' }}>
            <strong>Total ingresos:</strong>
            <strong>${totalIngresos.toFixed(2)}</strong>
          </div>
        </div>

        <div className="card">
          <div className="card-header"><strong>Gastos (detalle)</strong></div>
          <div className="item-list">
            <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', padding: '10px 0', borderBottom: '2px solid var(--border-color)', fontWeight: '600', color: '#7f8c8d' }}>
              <span>Concepto</span>
              <span>Importe</span>
            </div>
            {gastosFiltrados.map((g) => (
              <div key={`gas-${g.id}`} className="item-row" style={{ display: 'grid', gridTemplateColumns: '2fr 1fr' }}>
                <span>{g.tipo}</span>
                <span>${parseFloat(g.cantidad).toFixed(2)}</span>
              </div>
            ))}
            {gastosFiltrados.length === 0 && (
              <p style={{ padding: '20px', color: '#7f8c8d' }}>Sin gastos.</p>
            )}
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', borderTop: '1px solid var(--border-color)', paddingTop: '10px' }}>
            <strong>Total gastos:</strong>
            <strong>${totalGastos.toFixed(2)}</strong>
          </div>
        </div>
      </div>

      <div className="card" style={{ marginTop: '16px' }}>
        <div className="card-header"><strong>Balance</strong></div>
        <div style={{ display: 'flex', justifyContent: 'space-between' }}>
          <span>Total ingresos: ${totalIngresos.toFixed(2)}</span>
          <span>Total gastos: ${totalGastos.toFixed(2)}</span>
          <strong>Balance: ${balance.toFixed(2)}</strong>
        </div>
      </div>
    </div>
  );
};

export default ReportsPage;
