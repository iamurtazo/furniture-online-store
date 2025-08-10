export interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  discount?: number;
  image: string;
  category: string;
  onSale?: boolean;
}

export interface Category {
  id: number;
  name: string;
  slug: string;
}

export interface CartItem {
  id: number;
  productId: number;
  name: string;
  price: number;
  quantity: number;
  image: string;
  discount?: number;
}

export interface User {
  isAuthenticated: boolean;
  firstName?: string;
  username?: string;
  isStaff?: boolean;
}
