import { useEffect, useState } from 'react';
import axiosClient from '../../api/axiosClient';
import Table from '../../components/common/Table';
import Modal from '../../components/common/Modal';

const PayrollPage = () => {
  const [payrolls, setPayrolls] = useState([]);
  const [staff, setStaff] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentPayroll, setCurrentPayroll] = useState(null);
  const [filters, setFilters] = useState({ month: '', year: '' });
  const [formData, setFormData] = useState({
    atendente: '',
    year: new Date().getFullYear(),
    month: new Date().getMonth() + 1,
    salario_base: '',
    comision_fija_total: '',
    comision_porcentaje_total: '',
    otros: ''
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [resPayrolls, resStaff] = await Promise.all([
        axiosClient.get('/nomina/'),
        axiosClient.get('/atendente/')
      ]);
      setPayrolls(resPayrolls.data);
      setStaff(resStaff.data);
    } catch (error) {
      console.error('Error fetching payrolls:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    setFilters((prev) => ({ ...prev, [name]: value }));
  };

  const handleOpenModal = (payroll = null) => {
    if (payroll) {
      setCurrentPayroll(payroll);
      setFormData({
        atendente: payroll.atendente,
        year: payroll.year,
        month: payroll.month,
        salario_base: payroll.salario_base,
        comision_fija_total: payroll.comision_fija_total,
        comision_porcentaje_total: payroll.comision_porcentaje_total,
        otros: payroll.otros
      });
    } else {
      setCurrentPayroll(null);
      setFormData({
        atendente: '',
        year: new Date().getFullYear(),
        month: new Date().getMonth() + 1,
        salario_base: '',
        comision_fija_total: '',
        comision_porcentaje_total: '',
        otros: ''
      });
    }
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setCurrentPayroll(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const payload = {
        ...formData,
        atendente: parseInt(formData.atendente, 10),
        year: parseInt(formData.year, 10),
        month: parseInt(formData.month, 10)
      };

      if (currentPayroll) {
        await axiosClient.put(`/nomina/${currentPayroll.id}/`, payload);
      } else {
        await axiosClient.post('/nomina/', payload);
      }

      fetchData();
      handleCloseModal();
    } catch (error) {
      console.error('Error saving payroll:', error);
      alert('Error al guardar la nómina.');
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('¿Eliminar nómina?')) {
      try {
        await axiosClient.delete(`/nomina/${id}/`);
        fetchData();
      } catch (error) {
        console.error('Error deleting payroll:', error);
        alert('Error al eliminar la nómina.');
      }
    }
  };

  const handleRecalculate = async () => {
    try {
      await axiosClient.post('/nomina/recalcular/', {
        year: filters.year || new Date().getFullYear(),
        month: filters.month || new Date().getMonth() + 1,
      });
      fetchData();
    } catch (error) {
      console.error('Error recalculating payroll:', error);
      alert('Error al recalcular nóminas.');
    }
  };

  const staffById = new Map(staff.map((s) => [s.id, s]));

  const filteredPayrolls = payrolls.filter((p) => {
    if (filters.month && String(p.month) !== String(filters.month)) return false;
    if (filters.year && String(p.year) !== String(filters.year)) return false;
    return true;
  });

  const columns = [
    {
      key: 'atendente',
      header: 'Atendente',
      render: (value) => {
        const person = staffById.get(value);
        return person ? `${person.nombre} ${person.apellido}` : 'N/A';
      }
    },
    { key: 'month', header: 'Mes' },
    { key: 'year', header: 'Año' },
    { key: 'salario_base', header: 'Base' },
    { key: 'comision_fija_total', header: 'Comisión fija' },
    { key: 'comision_porcentaje_total', header: 'Comisión %' },
    { key: 'total', header: 'Total' }
  ];

  if (loading) {
    return <div className="loading">Cargando nóminas...</div>;
  }

  return (
    <div className="payroll-page">
      <div className="content-header">
        <h2>Nóminas</h2>
        <div style={{ display: 'flex', gap: '8px' }}>
          <button className="btn btn-secondary" onClick={handleRecalculate}>
            Recalcular
          </button>
          <button className="btn btn-primary" onClick={() => handleOpenModal()}>
            + Nueva Nómina
          </button>
        </div>
      </div>

      <div className="card">
        <div className="card-header" style={{ display: 'flex', gap: '10px' }}>
          <select name="month" className="form-input" value={filters.month} onChange={handleFilterChange}>
            <option value="">Mes</option>
            {Array.from({ length: 12 }, (_, i) => i + 1).map((m) => (
              <option key={m} value={m}>{m}</option>
            ))}
          </select>
          <input
            type="number"
            name="year"
            className="form-input"
            placeholder="Año"
            value={filters.year}
            onChange={handleFilterChange}
            style={{ maxWidth: '120px' }}
          />
        </div>

        <Table
          columns={columns}
          data={filteredPayrolls}
          onEdit={handleOpenModal}
          onDelete={handleDelete}
        />
      </div>

      <Modal
        isOpen={isModalOpen}
        onClose={handleCloseModal}
        title={currentPayroll ? 'Editar Nómina' : 'Nueva Nómina'}
      >
        <form onSubmit={handleSubmit} className="payroll-form">
          <div className="form-group">
            <label>Atendente</label>
            <select
              name="atendente"
              value={formData.atendente}
              onChange={handleInputChange}
              required
              className="form-input"
            >
              <option value="">Seleccionar atendente</option>
              {staff.map((member) => (
                <option key={member.id} value={member.id}>
                  {member.nombre} {member.apellido}
                </option>
              ))}
            </select>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>Mes</label>
              <input
                type="number"
                name="month"
                value={formData.month}
                onChange={handleInputChange}
                min="1"
                max="12"
                className="form-input"
                required
              />
            </div>
            <div className="form-group">
              <label>Año</label>
              <input
                type="number"
                name="year"
                value={formData.year}
                onChange={handleInputChange}
                className="form-input"
                required
              />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>Salario base</label>
              <input
                type="number"
                name="salario_base"
                value={formData.salario_base}
                onChange={handleInputChange}
                step="0.01"
                className="form-input"
              />
            </div>
            <div className="form-group">
              <label>Comisión fija</label>
              <input
                type="number"
                name="comision_fija_total"
                value={formData.comision_fija_total}
                onChange={handleInputChange}
                step="0.01"
                className="form-input"
              />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>Comisión %</label>
              <input
                type="number"
                name="comision_porcentaje_total"
                value={formData.comision_porcentaje_total}
                onChange={handleInputChange}
                step="0.01"
                className="form-input"
              />
            </div>
            <div className="form-group">
              <label>Otros</label>
              <input
                type="number"
                name="otros"
                value={formData.otros}
                onChange={handleInputChange}
                step="0.01"
                className="form-input"
              />
            </div>
          </div>

          <div className="form-actions">
            <button type="button" className="btn btn-secondary" onClick={handleCloseModal}>
              Cancelar
            </button>
            <button type="submit" className="btn btn-primary">
              {currentPayroll ? 'Actualizar' : 'Crear'}
            </button>
          </div>
        </form>
      </Modal>
    </div>
  );
};

export default PayrollPage;
