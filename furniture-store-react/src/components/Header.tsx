"use client";

import { useState } from "react";
import { Search, ShoppingCart, User, Menu, X, Home, Info } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { User as UserType } from "@/types";

interface HeaderProps {
    user: UserType;
    cartItemCount: number;
    onSearch: (query: string) => void;
    onLogout: () => void;
    onToggleCart: () => void;
}

export const Header: React.FC<HeaderProps> = ({ user, cartItemCount, onSearch, onLogout, onToggleCart }) => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const [isUserMenuOpen, setIsUserMenuOpen] = useState(false);
    const [searchQuery, setSearchQuery] = useState("");

    const handleSearch = (e: React.FormEvent) => {
        e.preventDefault();
        onSearch(searchQuery);
    };

    return (
        <header className="bg-gray-900 text-white shadow-lg sticky top-0 z-50">
            <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between items-center h-16">
                    {/* Logo */}
                    <motion.a href="/" className="flex items-center space-x-4 cursor-pointer" whileHover={{ scale: 1.05 }}>
                        <Home size={24} />
                        <span className="text-xl font-bold">FurnitureStore</span>
                    </motion.a>

                    {/* Desktop Navigation */}
                    <div className="hidden md:flex items-center space-x-8">
                        {/* Info Dropdown */}
                        <div className="relative group">
                            <button className="flex items-center space-x-1 hover:text-gray-300 transition-colors">
                                <Info size={16} />
                                <span>Information</span>
                            </button>

                            <div className="absolute top-full left-0 mt-2 w-56 bg-white text-gray-800 rounded-lg shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
                                <div className="py-2">
                                    <a href="/delivery" className="block px-4 py-2 hover:bg-gray-100 transition-colors">
                                        Delivery and Payment
                                    </a>
                                    <a href="/contact" className="block px-4 py-2 hover:bg-gray-100 transition-colors">
                                        Contact Information
                                    </a>
                                    <a href="/about" className="block px-4 py-2 hover:bg-gray-100 transition-colors">
                                        About Us
                                    </a>
                                </div>
                            </div>
                        </div>

                        {/* Cart */}
                        <motion.button className="relative flex items-center space-x-1 hover:text-gray-300 transition-colors" whileHover={{ scale: 1.05 }} onClick={onToggleCart}>
                            <ShoppingCart size={20} />
                            <span>Cart</span>
                            {cartItemCount > 0 && (
                                <motion.span
                                    className="absolute -top-2 -right-2 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center"
                                    initial={{ scale: 0 }}
                                    animate={{ scale: 1 }}
                                    transition={{ type: "spring", stiffness: 500 }}
                                >
                                    {cartItemCount}
                                </motion.span>
                            )}
                        </motion.button>

                        {/* User Menu */}
                        {user.isAuthenticated ? (
                            <div className="relative">
                                <button className="flex items-center space-x-2 hover:text-gray-300 transition-colors" onClick={() => setIsUserMenuOpen(!isUserMenuOpen)}>
                                    <User size={16} />
                                    <span>Hi, {user.firstName || user.username}</span>
                                </button>

                                <AnimatePresence>
                                    {isUserMenuOpen && (
                                        <motion.div
                                            className="absolute top-full right-0 mt-2 w-48 bg-white text-gray-800 rounded-lg shadow-lg"
                                            initial={{ opacity: 0, y: -10 }}
                                            animate={{ opacity: 1, y: 0 }}
                                            exit={{ opacity: 0, y: -10 }}
                                            transition={{ duration: 0.2 }}
                                        >
                                            <div className="py-2">
                                                <button onClick={onToggleCart} className="block w-full text-left px-4 py-2 hover:bg-gray-100 transition-colors">
                                                    My Cart
                                                </button>
                                                <a href="#" className="block px-4 py-2 hover:bg-gray-100 transition-colors">
                                                    Personal Account
                                                </a>
                                                {user.isStaff && (
                                                    <a href="#" className="block px-4 py-2 hover:bg-gray-100 transition-colors">
                                                        Admin Panel
                                                    </a>
                                                )}
                                                <hr className="my-1" />
                                                <button onClick={onLogout} className="block w-full text-left px-4 py-2 hover:bg-gray-100 transition-colors">
                                                    Logout
                                                </button>
                                            </div>
                                        </motion.div>
                                    )}
                                </AnimatePresence>
                            </div>
                        ) : (
                            <div className="flex items-center space-x-4">
                                <motion.button className="flex items-center space-x-1 hover:text-gray-300 transition-colors" whileHover={{ scale: 1.05 }}>
                                    <User size={16} />
                                    <span>Login</span>
                                </motion.button>
                                <motion.button className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-lg transition-colors" whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>
                                    Register
                                </motion.button>
                            </div>
                        )}
                    </div>

                    {/* Search Bar */}
                    <form onSubmit={handleSearch} className="hidden md:flex items-center">
                        <div className="relative">
                            <input
                                type="text"
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                                placeholder="Search furniture..."
                                className="bg-gray-800 text-white placeholder-gray-400 px-4 py-2 pr-10 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                            />
                            <button type="submit" className="absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-white transition-colors">
                                <Search size={18} />
                            </button>
                        </div>
                    </form>

                    {/* Mobile Menu Button */}
                    <button className="md:hidden" onClick={() => setIsMenuOpen(!isMenuOpen)}>
                        {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
                    </button>
                </div>

                {/* Mobile Menu */}
                <AnimatePresence>
                    {isMenuOpen && (
                        <motion.div
                            className="md:hidden bg-gray-800 rounded-lg mt-2 mb-4"
                            initial={{ opacity: 0, height: 0 }}
                            animate={{ opacity: 1, height: "auto" }}
                            exit={{ opacity: 0, height: 0 }}
                            transition={{ duration: 0.3 }}
                        >
                            <div className="px-4 py-4 space-y-4">
                                {/* Mobile Search */}
                                <form onSubmit={handleSearch} className="flex">
                                    <input
                                        type="text"
                                        value={searchQuery}
                                        onChange={(e) => setSearchQuery(e.target.value)}
                                        placeholder="Search..."
                                        className="flex-1 bg-gray-700 text-white placeholder-gray-400 px-3 py-2 rounded-l-lg focus:outline-none"
                                    />
                                    <button type="submit" className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-r-lg transition-colors">
                                        <Search size={18} />
                                    </button>
                                </form>

                                {/* Mobile Navigation Links */}
                                <div className="space-y-2">
                                    <div className="space-y-1">
                                        <a href="/delivery" className="block w-full text-left py-2 hover:text-gray-300 transition-colors">
                                            Delivery & Payment
                                        </a>
                                        <a href="/contact" className="block w-full text-left py-2 hover:text-gray-300 transition-colors">
                                            Contact Info
                                        </a>
                                        <a href="/about" className="block w-full text-left py-2 hover:text-gray-300 transition-colors">
                                            About Us
                                        </a>
                                    </div>
                                    <button onClick={onToggleCart} className="block w-full text-left py-2 hover:text-gray-300 transition-colors flex items-center">
                                        <ShoppingCart size={16} className="mr-2" />
                                        Cart {cartItemCount > 0 && `(${cartItemCount})`}
                                    </button>

                                    {user.isAuthenticated ? (
                                        <>
                                            <button className="block w-full text-left py-2 hover:text-gray-300 transition-colors">Personal Account</button>
                                            <button onClick={onLogout} className="block w-full text-left py-2 hover:text-gray-300 transition-colors">
                                                Logout
                                            </button>
                                        </>
                                    ) : (
                                        <>
                                            <button className="block w-full text-left py-2 hover:text-gray-300 transition-colors">Login</button>
                                            <button className="block w-full text-left py-2 bg-blue-600 hover:bg-blue-700 rounded text-center transition-colors">Register</button>
                                        </>
                                    )}
                                </div>
                            </div>
                        </motion.div>
                    )}
                </AnimatePresence>
            </nav>
        </header>
    );
};
