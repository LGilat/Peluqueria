import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from '../context/AuthContext';
import LoginPage from '../pages/Auth/LoginPage';
import DashboardPage from '../pages/Dashboard/DashboardPage';
import ClientListPage from '../pages/Clients/ClientListPage';
import ClientDetailPage from '../pages/Clients/ClientDetailPage';
import ReservationListPage from '../pages/Reservations/ReservationListPage';
import StaffListPage from '../pages/Staff/StaffListPage';
import ServiceListPage from '../pages/Services/ServiceListPage';
import ProductListPage from '../pages/Products/ProductListPage';
import CalendarPage from '../pages/Calendar/CalendarPage';
import MainLayout from '../components/Layout/MainLayout';

const ProtectedRoute = ({ children }) => {
  const { isAuthenticated, loading } = useAuth();

  if (loading) {
    return <div>Cargando...</div>;
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return children;
};

const PublicRoute = ({ children }) => {
  const { isAuthenticated, loading } = useAuth();

  if (loading) {
    return <div>Cargando...</div>;
  }

  if (isAuthenticated) {
    return <Navigate to="/" replace />;
  }

  return children;
};

const AppRoutes = () => {
  return (
    <Routes>
      <Route
        path="/login"
        element={
          <PublicRoute>
            <LoginPage />
          </PublicRoute>
        }
      />

      <Route
        path="/"
        element={
          <ProtectedRoute>
            <MainLayout />
          </ProtectedRoute>
        }
      >
        <Route index element={<DashboardPage />} />
        <Route path="clients" element={<ClientListPage />} />
        <Route path="clients/:id" element={<ClientDetailPage />} />
        <Route path="reservations" element={<ReservationListPage />} />
        <Route path="calendar" element={<CalendarPage />} />
        <Route path="staff" element={<StaffListPage />} />
        <Route path="services" element={<ServiceListPage />} />
        <Route path="products" element={<ProductListPage />} />

        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
  );
};

const AppRouter = () => {
  return (
    <Router>
      <AuthProvider>
        <AppRoutes />
      </AuthProvider>
    </Router>
  );
};

export default AppRouter;
