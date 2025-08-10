import { create } from 'zustand';
import { CartItem, Product, User } from '@/types';

interface StoreState {
  // Cart state
  cart: CartItem[];
  cartOpen: boolean;
  
  // User state
  user: User;
  
  // Wishlist state
  wishlist: number[];
  
  // UI state
  searchQuery: string;
  selectedCategory: string;
  
  // Actions
  addToCart: (product: Product) => void;
  removeFromCart: (id: number) => void;
  updateCartQuantity: (id: number, quantity: number) => void;
  toggleCart: () => void;
  closeCart: () => void;
  
  toggleWishlist: (productId: number) => void;
  
  setSearchQuery: (query: string) => void;
  setSelectedCategory: (category: string) => void;
  
  login: (user: User) => void;
  logout: () => void;
}

export const useStore = create<StoreState>((set, get) => ({
  // Initial state
  cart: [],
  cartOpen: false,
  user: { isAuthenticated: false },
  wishlist: [],
  searchQuery: '',
  selectedCategory: 'all',
  
  // Cart actions
  addToCart: (product: Product) => {
    const { cart } = get();
    const existingItem = cart.find(item => item.productId === product.id);
    
    if (existingItem) {
      set({
        cart: cart.map(item =>
          item.productId === product.id
            ? { ...item, quantity: item.quantity + 1 }
            : item
        )
      });
    } else {
      const newCartItem: CartItem = {
        id: Date.now(), // Simple ID generation
        productId: product.id,
        name: product.name,
        price: product.price,
        quantity: 1,
        image: product.image,
        discount: product.discount,
      };
      set({ cart: [...cart, newCartItem] });
    }
  },
  
  removeFromCart: (id: number) => {
    const { cart } = get();
    set({ cart: cart.filter(item => item.id !== id) });
  },
  
  updateCartQuantity: (id: number, quantity: number) => {
    if (quantity < 1) return;
    const { cart } = get();
    set({
      cart: cart.map(item =>
        item.id === id ? { ...item, quantity } : item
      )
    });
  },
  
  toggleCart: () => {
    const { cartOpen } = get();
    set({ cartOpen: !cartOpen });
  },
  
  closeCart: () => {
    set({ cartOpen: false });
  },
  
  // Wishlist actions
  toggleWishlist: (productId: number) => {
    const { wishlist } = get();
    if (wishlist.includes(productId)) {
      set({ wishlist: wishlist.filter(id => id !== productId) });
    } else {
      set({ wishlist: [...wishlist, productId] });
    }
  },
  
  // Search and filter actions
  setSearchQuery: (query: string) => {
    set({ searchQuery: query });
  },
  
  setSelectedCategory: (category: string) => {
    set({ selectedCategory: category });
  },
  
  // User actions
  login: (user: User) => {
    set({ user });
  },
  
  logout: () => {
    set({ user: { isAuthenticated: false } });
  },
}));
