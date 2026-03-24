import { useEffect, useMemo, useState } from 'react';
import axiosClient from '../../api/axiosClient';

const LedgerPage = () => {
  const [ingresos, setIngresos] = useState([]);
  const [gastos, setGastos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [year, setYear] = useState(new Date().getFullYear());

  useEffect(() => {
    fetchData();
  }, [year]);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [resIngresos, resGastos] = await Promise.all([
        axiosClient.get('/ingreso/'),
        axiosClient.get('/gasto/')
      ]);
      setIngresos(resIngresos.data);
      setGastos(resGastos.data);
    } catch (error) {
      console.error('Error fetching ledger:', error);
    } finally {
      setLoading(false);
    }
  };

  const ingresosFiltrados = useMemo(
    () => ingresos.filter((i) => new Date(i.fecha).getFullYear() === Number(year)),
    [ingresos, year]
  );

  const gastosFiltrados = useMemo(
    () => gastos.filter((g) => new Date(g.fecha).getFullYear() === Number(year)),
    [gastos, year]
  );

  const totalIngresos = ingresosFiltrados.reduce((sum, i) => sum + parseFloat(i.cantidad), 0);
  const totalGastos = gastosFiltrados.reduce((sum, g) => sum + parseFloat(g.cantidad), 0);
  const balance = totalIngresos - totalGastos;

  if (loading) {
    return <div className="loading">Cargando contabilidad...</div>;
  }

  return (
    <div className="ledger-page">
      <div className="content-header">
        <h2>Contabilidad</h2>
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
          <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr 1fr', padding: '10px 0', borderBottom: '2px solid var(--border-color)', fontWeight: '600', color: '#7f8c8d' }}>
            <span>Concepto</span>
            <span>Tipo</span>
            <span>Importe</span>
          </div>

          {ingresosFiltrados.map((i) => (
            <div key={`ingreso-${i.id}`} className="item-row" style={{ display: 'grid', gridTemplateColumns: '2fr 1fr 1fr' }}>
              <span>{i.tipo}</span>
              <span>Ingreso</span>
              <span>${parseFloat(i.cantidad).toFixed(2)}</span>
            </div>
          ))}

          {gastosFiltrados.map((g) => (
            <div key={`gasto-${g.id}`} className="item-row" style={{ display: 'grid', gridTemplateColumns: '2fr 1fr 1fr' }}>
              <span>{g.tipo}</span>
              <span>Gasto</span>
              <span>${parseFloat(g.cantidad).toFixed(2)}</span>
            </div>
          ))}
        </div>

        <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '16px' }}>
          <strong>Total ingresos: ${totalIngresos.toFixed(2)}</strong>
          <strong>Total gastos: ${totalGastos.toFixed(2)}</strong>
          <strong>Balance: ${balance.toFixed(2)}</strong>
        </div>
      </div>
    </div>
  );
};

export default LedgerPage;
