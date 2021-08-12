import { render, screen } from '@testing-library/react';
import App_init from './App_init';

test('renders learn react link', () => {
  render(<App_init />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
