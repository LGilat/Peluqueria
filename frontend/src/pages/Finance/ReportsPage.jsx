import { useEffect, useMemo, useState } from 'react';
import axiosClient from '../../api/axiosClient';

const ReportsPage = () => {
  const [data, setData] = useState([]);
  const [year, setYear] = useState(new Date().getFullYear());
  const [compareYear, setCompareYear] = useState(year - 1);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchReports();
  }, [year, compareYear]);

  const fetchReports = async () => {
    try {
      setLoading(true);
      const [resCurrent, resCompare] = await Promise.all([
        axiosClient.get(`/reportes-financieros/?year=${year}`),
        axiosClient.get(`/reportes-financieros/?year=${compareYear}`)
      ]);

      const current = resCurrent.data.data || [];
      const previous = resCompare.data.data || [];

      setData({ current, previous });
    } catch (error) {
      console.error('Error fetching reports:', error);
    } finally {
      setLoading(false);
    }
  };

  const currentByMonth = useMemo(() => {
    const map = new Map();
    (data.current || []).forEach((row) => map.set(row.month, row));
    return map;
  }, [data]);

  const previousByMonth = useMemo(() => {
    const map = new Map();
    (data.previous || []).forEach((row) => map.set(row.month, row));
    return map;
  }, [data]);

  const maxValue = Math.max(
    1,
    ...[...(data.current || []), ...(data.previous || [])].map((row) => row.ingresos || 0)
  );

  if (loading) {
    return <div className="loading">Cargando reportes...</div>;
  }

  return (
    <div className="reports-page">
      <div className="content-header">
        <h2>Reportes Financieros</h2>
        <div style={{ display: 'flex', gap: '8px' }}>
          <input
            type="number"
            className="form-input"
            value={year}
            onChange={(e) => setYear(parseInt(e.target.value, 10))}
            style={{ maxWidth: '120px' }}
          />
          <input
            type="number"
            className="form-input"
            value={compareYear}
            onChange={(e) => setCompareYear(parseInt(e.target.value, 10))}
            style={{ maxWidth: '120px' }}
          />
        </div>
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
            <span>Comparativa</span>
          </div>

          {Array.from({ length: 12 }, (_, i) => i + 1).map((month) => {
            const row = currentByMonth.get(month) || {
              ingresos: 0,
              gastos: 0,
              margen: 0,
              ingresos_servicios: 0,
              ingresos_productos: 0
            };
            const prev = previousByMonth.get(month) || { ingresos: 0 };

            return (
              <div key={month} className="item-row" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr 1fr 1fr 2fr', alignItems: 'center' }}>
                <span>{month}/{year}</span>
                <span>${parseFloat(row.ingresos).toFixed(2)}</span>
                <span>${parseFloat(row.gastos).toFixed(2)}</span>
                <span>${parseFloat(row.margen).toFixed(2)}</span>
                <span>${parseFloat(row.ingresos_servicios).toFixed(2)}</span>
                <span>${parseFloat(row.ingresos_productos).toFixed(2)}</span>
                <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
                  <div
                    title={`Ingresos ${year}: ${row.ingresos}`}
                    style={{
                      height: '10px',
                      width: `${(row.ingresos / maxValue) * 100}%`,
                      background: '#27ae60',
                      borderRadius: '6px'
                    }}
                  />
                  <div
                    title={`Ingresos ${compareYear}: ${prev.ingresos}`}
                    style={{
                      height: '10px',
                      width: `${(prev.ingresos / maxValue) * 100}%`,
                      background: '#2980b9',
                      borderRadius: '6px'
                    }}
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default ReportsPage;
