import { useEffect, useMemo, useState } from 'react';
import axiosClient from '../../api/axiosClient';
import './CalendarPage.css';

const startOfWeek = (date) => {
  const d = new Date(date);
  const day = d.getDay();
  const diff = (day === 0 ? -6 : 1) - day; // Monday start
  d.setDate(d.getDate() + diff);
  d.setHours(0, 0, 0, 0);
  return d;
};

const addDays = (date, days) => {
  const d = new Date(date);
  d.setDate(d.getDate() + days);
  return d;
};

const formatDate = (date) => {
  return date.toISOString().slice(0, 10);
};

const formatLabel = (date) => {
  return date.toLocaleDateString('es-ES', { weekday: 'short', day: 'numeric', month: 'short' });
};

const CalendarPage = () => {
  const [reservations, setReservations] = useState([]);
  const [services, setServices] = useState([]);
  const [clients, setClients] = useState([]);
  const [staff, setStaff] = useState([]);
  const [loading, setLoading] = useState(true);
  const [weekStart, setWeekStart] = useState(startOfWeek(new Date()));

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [resReservations, resServices, resClients, resStaff] = await Promise.all([
        axiosClient.get('/reserva/'),
        axiosClient.get('/servicio/'),
        axiosClient.get('/cliente/'),
        axiosClient.get('/atendente/')
      ]);
      setReservations(resReservations.data);
      setServices(resServices.data);
      setClients(resClients.data);
      setStaff(resStaff.data);
    } catch (error) {
      console.error('Error fetching calendar data:', error);
    } finally {
      setLoading(false);
    }
  };

  const serviceById = useMemo(() => new Map(services.map((s) => [s.id, s])), [services]);
  const clientById = useMemo(() => new Map(clients.map((c) => [c.id, c])), [clients]);
  const staffById = useMemo(() => new Map(staff.map((s) => [s.id, s])), [staff]);

  const days = Array.from({ length: 7 }, (_, i) => addDays(weekStart, i));
  const reservationsByDate = useMemo(() => {
    const map = new Map();
    days.forEach((d) => map.set(formatDate(d), []));

    reservations.forEach((res) => {
      if (!map.has(res.fecha)) return;
      map.get(res.fecha).push(res);
    });

    for (const list of map.values()) {
      list.sort((a, b) => a.hora.localeCompare(b.hora));
    }

    return map;
  }, [reservations, days]);

  const handlePrevWeek = () => setWeekStart(addDays(weekStart, -7));
  const handleNextWeek = () => setWeekStart(addDays(weekStart, 7));

  if (loading) {
    return <div className="loading">Cargando calendario...</div>;
  }

  return (
    <div className="calendar-page">
      <div className="content-header">
        <h2>Calendario</h2>
        <div style={{ display: 'flex', gap: '8px' }}>
          <button className="btn btn-secondary" onClick={handlePrevWeek}>Semana anterior</button>
          <button className="btn btn-secondary" onClick={handleNextWeek}>Semana siguiente</button>
        </div>
      </div>

      <div className="calendar-grid">
        {days.map((day) => {
          const key = formatDate(day);
          const items = reservationsByDate.get(key) || [];
          return (
            <div key={key} className="calendar-day">
              <div className="calendar-day-header">
                {formatLabel(day)}
              </div>
              {items.length === 0 ? (
                <div className="calendar-empty">Sin reservas</div>
              ) : (
                items.map((res) => {
                  const servicio = serviceById.get(res.servicio);
                  const cliente = clientById.get(res.cliente);
                  const atendente = staffById.get(res.atendente);
                  return (
                    <div key={res.id} className={`calendar-item status-${res.estado}`}>
                      <div className="calendar-time">{res.hora.slice(0, 5)}</div>
                      <div className="calendar-title">
                        {servicio ? servicio.nombre : 'Servicio'}
                      </div>
                      <div className="calendar-meta">
                        {cliente ? `${cliente.nombre} ${cliente.apellido}` : `Cliente ${res.cliente}`}
                      </div>
                      <div className="calendar-meta">
                        {atendente ? `${atendente.nombre} ${atendente.apellido}` : 'Sin atendente'}
                      </div>
                    </div>
                  );
                })
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default CalendarPage;
